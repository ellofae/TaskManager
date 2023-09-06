from controllers.company_controller import get_company_controller
from controllers.company_user_controller import get_company_user_controller
from controllers.subtask_controller import get_subtask_controller
from controllers.task_controller import get_task_controller
from controllers.token_controller import get_token_controller
from controllers.user_controller import get_user_controller

user_controller = get_user_controller()
company_controller = get_company_controller()
task_controller = get_task_controller()
subtask_controller = get_subtask_controller()
company_user_controller = get_company_user_controller()
token_controller = get_token_controller()
