import click
from logbook_processor.processor.processors import LogbookListProcessor
from logbook_processor.processor.utils import generate_file_name, get_waypoints_from_json, save_trips


@click.command()
@click.option("--waypoint_file", help="Waypoints List")
def run(waypoint_file):
    if waypoint_file:
        waypoints = get_waypoints_from_json(waypoint_file)
        processor = LogbookListProcessor(tuple(waypoints))
        trip_list = processor.get_trips()
        file_name = generate_file_name()
        save_trips(file_name, trip_list)


if __name__ == "__main__":
    run()
