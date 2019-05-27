# LogbookProcessor

LogbookProcessor is a tool for processing location data!

LogbookProcessor makes it easy to process large quantities of location data into a cohesive and comprehensible! Automatically puts together trips, calculating distance and taking into consideration not only common interruptions such as redlights, trafic jams but also geocoordinates jumps and inacurracy to turn this:
```
[
  {
    "lat": 51.54987,
    "timestamp": "2018-08-10T20:00:00Z",
    "lng": 12.41039
  },
  {
    "lat": 55.54769,
    "timestamp": "2018-08-10T21:00:00Z",
    "lng": 14.94316
  }
]
```

Into this:

```
[
  {
    "start": {
      "timestamp": "2018-08-10T20:00:00Z",
      "lat": 51.54987,
      "lng": 12.41039
    },
    "end": {
      "timestamp": "2018-08-10T21:00:00Z",
      "lat": 55.54769,
      "lng": 14.94316
    },
    "distance": 475479
  }
]
```



# How to use it

1 - Clone project

`git clone git@github.com:Ghallz/LogbookProcessor.git`

2 - Install [Pipenv](https://github.com/pypa/pipenv)

3 - On project folder, install dependencies

`pipenv install`

4 - Start environment

`pipenv shell`

5 - Run command using path of file to be processed

`python cli.py --waypoint_file=PATH_TO_FILE`

6 - Check file created on data folder
