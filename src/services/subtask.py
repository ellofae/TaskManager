import repository.subtask as repo
import services.company_user as company_user_service
import services.task as task_service
from models.subtask import Subtask, SubtaskCreationForm

def create(subtask: SubtaskCreationForm, current_user_id) -> Subtask:
    #task = task_service.get_task_by_id(subtask.tasl, current_user_id)
    #company_user = company_user_service.check_weather_user_exists(current_user_id, task.company)
    #assert company_user, f'User is not attached to company with id {task.company}'
    pass