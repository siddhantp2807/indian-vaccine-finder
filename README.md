# indian-vaccine-finder

Python Script that searches for and sends desktop notifications if vaccines are available in your district.


First, install the `plyer` and the `requests` python packages.

```
pip install plyer requests

```

Next, inside of the `app.py` file, change the district name to districts near you.

```
districts = [
    "your-district-name"
]

```

After that to find vaccines, run

```
python app.py -a=49 -d=1 -f -t=30

```
This command searches for vaccines for a person of age 49, requiring Dose 1, requiring only notifications 
of free dose and enabling new notifications every 30 seconds from the notifier.




