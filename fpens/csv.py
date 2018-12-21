import csv

from django.utils import timezone

from .forms import PenForm


def import_csv(filename):
	rows = open(filename)
	records_added = 0
	errors = []
	for row in csv.DictReader(rows, delimiter=","):
	
		form = PenForm(row)
		if form.is_valid():
			model_instance = form.save(commit=False)
			model_instance.timestamp = timezone.now()
			model_instance.save()
			records_Added += 1
		else:
			errors.append(form.errors)
	
	return records_added, errors
