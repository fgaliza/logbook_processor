import click
from logbook_processor.processor.processors import LogbookStreamProcessor
from logbook_processor.processor.utils import generate_file_name, get_waypoints_from_json, save_trips
from progress.bar import FillingSquaresBar


@click.command()
@click.option("--waypoint_file", help="Waypoints List")
def run(waypoint_file):
    if waypoint_file:
        trip_list = []
        processor = LogbookStreamProcessor()
        waypoints = get_waypoints_from_json(waypoint_file)
        bar = FillingSquaresBar("Processing", max=len(waypoints))
        for waypoint in waypoints:
            trip = processor.process_waypoint(waypoint)
            if trip:
                trip_list.append(trip)
                processor.last_valid_waypoint = waypoint
            bar.next()

        file_name = generate_file_name()
        save_trips(file_name, trip_list)


if __name__ == "__main__":
    run()
