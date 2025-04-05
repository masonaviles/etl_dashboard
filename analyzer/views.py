import pandas as pd
import numpy as np
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CSVUploadForm
from .models import UploadSession, AnalysisResult

def upload_view(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            session = form.save(commit=False)
            session.original_filename = request.FILES['file'].name
            session.save()

            # Load and clean data
            df = pd.read_csv(session.file.path)

            # Optional: Basic data cleanup
            df = df.replace(['N/A', 'n/a', '', '~', ' ~'], np.nan, regex=True)
            df = df.apply(lambda col: pd.to_numeric(col, errors='ignore'))  # convert valid numerics

            # Safely compute mode
            modes_df = df.mode(numeric_only=True)
            mode_result = modes_df.iloc[0].to_dict() if not modes_df.empty else {}

            # Value counts: safe for dirty categorical data
            value_counts = {
                col: df[col].value_counts(dropna=False).head(3).to_dict()
                for col in df.columns
            }

            # Save analysis
            analysis = AnalysisResult(
                session=session,
                mean=df.mean(numeric_only=True).to_dict(),
                mode=mode_result,
                value_counts=value_counts,
                null_counts=df.isnull().sum().to_dict(),
                dtypes=df.dtypes.astype(str).to_dict(),
                duplicates_removed=df.duplicated().sum()
            )
            analysis.save()

            return redirect('analyzer:results', session_id=session.id)
    else:
        form = CSVUploadForm()
    return render(request, 'analyzer/upload.html', {'form': form})

def result_view(request, session_id):
    session = get_object_or_404(UploadSession, id=session_id)
    result = get_object_or_404(AnalysisResult, session=session)
    return render(request, 'analyzer/result.html', {
        'session': session,
        'result': result
    })
