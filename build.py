from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from markdown import markdown

SOURCES = Path.cwd() / "src"
TEMPLATE = SOURCES / "_template.html"
FILES = {"Finding the Truth in a Internet of Lies": SOURCES / "index.md"}
ENVIRONMENT = Environment(loader=FileSystemLoader(SOURCES))


def render(title, file):
    text = file.read_text()
    html = markdown(text)
    transformed = f"""
    {{% extends "{TEMPLATE.relative_to(SOURCES)}" %}}
    {{% block title %}}
        {title} | Convoluta
    {{% endblock %}}
    {{% block body %}}
        {html}
    {{% endblock %}}
    """
    template = ENVIRONMENT.from_string(transformed)

    return template.render()


if __name__ == "__main__":
    for title, file in FILES.items():
        path = Path.cwd() / f"{file.stem}.html"
        path.write_text(render(title, file))
