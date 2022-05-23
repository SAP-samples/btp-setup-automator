import jinja2
import logging

log = logging.getLogger(__name__)


def renderTemplateWithJson(templateFilename, targetFilename, parameters):

    templateLoader = jinja2.FileSystemLoader(searchpath="./libs/json/templates/")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(templateFilename)

    renderedText = template.render(parameters)  # this is where to put args to the template renderer

    with open(targetFilename, 'w') as f:
        f.write(renderedText)
