"""
AlphaLens API Routes
"""

from __future__ import annotations

import os
import tempfile
import traceback

import pandas as pd
import numpy as np

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.pipeline import run
from app.schemas import AnalysisResponse


router = APIRouter(
    prefix="/api",
    tags=["Analysis"],
)


def make_json_serializable(obj):
    """
    Convert numpy objects into JSON-compatible objects.
    """

    if isinstance(obj, dict):

        return {
            key: make_json_serializable(value)
            for key, value in obj.items()
        }


    if isinstance(obj, list):

        return [
            make_json_serializable(item)
            for item in obj
        ]


    if isinstance(obj, np.ndarray):

        return obj.tolist()


    if isinstance(obj, np.generic):

        return obj.item()


    return obj



@router.get("/ping")
def ping():

    return {
        "message": "AlphaLens API is working",
    }



@router.post(
    "/analyze",
    response_model=AnalysisResponse,
)
async def analyze(

    portfolio_file: UploadFile = File(...),

    factor_file: UploadFile | None = File(None),

):

    portfolio_path = None
    factor_data = None


    try:

        # -----------------------------
        # Save portfolio file
        # -----------------------------

        portfolio_suffix = os.path.splitext(
            portfolio_file.filename
        )[1]


        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=portfolio_suffix,
        ) as tmp:

            tmp.write(
                await portfolio_file.read()
            )

            portfolio_path = tmp.name



        # -----------------------------
        # Load optional factor file
        # -----------------------------

        if factor_file:

            factor_suffix = os.path.splitext(
                factor_file.filename
            )[1]


            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=factor_suffix,
            ) as factor_tmp:


                factor_tmp.write(
                    await factor_file.read()
                )

                factor_path = factor_tmp.name



            factor_data = pd.read_csv(
                factor_path,
                parse_dates=True,
                index_col=0,
            )


            os.remove(factor_path)



        # -----------------------------
        # Run AlphaLens
        # -----------------------------

        result = run(
            portfolio_path,
            factor_data=factor_data,
            generate_charts=True,
            generate_html=False,
            verbose=False,
        )


        charts = {

            name: figure.to_plotly_json()

            for name, figure
            in result.charts.items()

        }



        return AnalysisResponse(

            dataset_type=result.dataset_type,

            frequency=result.frequency.name,

            observations=len(result.returns),

            metrics=make_json_serializable(
                result.metrics
            ),

            charts=make_json_serializable(
                charts
            ),

            metadata=make_json_serializable(
                result.metadata
            ),

        )


    except Exception as exc:


        traceback.print_exc()


        raise HTTPException(

            status_code=500,

            detail=str(exc),

        )


    finally:


        if portfolio_path and os.path.exists(
            portfolio_path
        ):

            os.remove(
                portfolio_path
            )