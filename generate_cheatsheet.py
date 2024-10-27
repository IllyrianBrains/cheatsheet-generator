import json
import argparse
from jinja2 import Environment, FileSystemLoader

def main(template_path, config_path, output_path):
    # Load configuration from JSON file
    with open(config_path) as config_file:
        cheatsheet_data = json.load(config_file)

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_path)
    output = template.render(**cheatsheet_data)

    # Save the output as an HTML file
    with open(output_path, "w") as file:
        file.write(output)

    print(f"Cheatsheet generated successfully: {output_path}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate a mentor-mentee cheatsheet HTML file.")
    parser.add_argument(
        "--template",
        default="templates/simple_template.html",
        help="Path to the Jinja2 template file (default: templates/simple_template.html)"
    )
    parser.add_argument(
        "--config",
        default="examples/disaster_resilience.json",
        help="Path to the configuration JSON file (default: example/disaster_resilience.json)"
    )
    parser.add_argument(
        "-o", "--output",
        default="test_run.html",
        help="Output HTML file name"
    )

    args = parser.parse_args()
    main(args.template, args.config, args.output)
