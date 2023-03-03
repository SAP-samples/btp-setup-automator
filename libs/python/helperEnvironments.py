import logging
import time

from libs.python.helperCommandExecution import runShellCommand
from libs.python.helperJson import convertStringToJson

log = logging.getLogger(__name__)


def check_if_service_plan_supported_in_environment(btpUsecase, service, environment):
    result = False
    # Defines how often we should ask sapbtp whether the plan is
    # available or not
    MAX_TRIES = 2
    # Seconds after which we should try again
    SEARCH_EVERY_X_SECONDS = 5

    command = (
        "btp --format json list services/plan"
        + " --subaccount "
        + btpUsecase.accountMetadata.get("subaccountid")
        + " --environment "
        + environment
    )
    message = (
        "Check if service >"
        + service.name
        + "< and plan >"
        + service.plan
        + "<"
        + " is supported in this sub account for the environment >sapbtp<"
    )

    for x in range(MAX_TRIES):
        p = runShellCommand(btpUsecase, command, "INFO", message)
        returnMessage = p.stdout.decode()
        jsonResult = convertStringToJson(returnMessage)

        for entry in jsonResult:
            if (
                entry.get("service_offering_name") == service.name
                and entry.get("catalog_name") == service.plan
            ):
                return True
        log.info(jsonResult)
        # In case the search was not successful, sleep a few seconds before trying again
        log.info(
            "Plan not found, yet. Trying again ("
            + str(x)
            + "/"
            + str(MAX_TRIES)
            + ") in "
            + str(SEARCH_EVERY_X_SECONDS)
            + "seconds."
        )
        time.sleep(SEARCH_EVERY_X_SECONDS)

    return result
