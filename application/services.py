# application/services.py
from application.models import Interviewer, Interviewee, Interview
import datetime


def create_interviewer(request_data):
    name = str(request_data.get('name', ''))
    department = str(request_data.get('department', ''))
    if name and department:
        interviewer = Interviewer(name=name, department=department)
        interviewer.save()
        response = {
            'id': interviewer.id,
            'name': interviewer.name,
            'department': interviewer.department,
        }
    else:
        response = {
            'error_message': 'Name or Department are blank.'
        }
    return response


def create_interviewee(request_data):
    name = str(request_data.get('name', ''))
    email = str(request_data.get('email', ''))
    linked_in = str(request_data.get('linked_in', ''))
    if name and email and linked_in:
        interviewee = Interviewee(name=name, email=email, linked_in=linked_in)
        interviewee.save()
        response = {
            'id': interviewee.id,
            'name': interviewee.name,
            'email': interviewee.department,
            'linked_in': interviewee.linked_in
        }
    else:
        response = {
            'error_message': 'Name or Email or LinkedIn URL are blank.'
        }
    return response


def create_interview(request_data):
    interviewer_id = str(request_data.get('interviewer_id', ''))
    interviewee_id = str(request_data.get('interviewee_id', ''))
    start_time_str = str(request_data.get('start_time', ''))
    end_time_str = str(request_data.get('start_time', ''))
    start_time = datetime.datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S.%f')
    end_time = datetime.datetime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S.%f')
    if interviewee_id and interviewer_id and start_time_str and end_time_str:
        interview = Interview(interviewee_id=interviewee_id, interviewer_id=interviewer_id,
                              start_time=start_time, end_time=end_time)
        interview.save()
        response = {
            'interviewer_id': interviewer_id,
            'interviewee_id': interviewee_id,
            'start_time_str': start_time_str,
            'end_time_str': start_time_str
        }
    else:
        response = {
            'error_message': 'Interviewee or Interviewer or Start and End times missing'
        }
    return response


def list_interviewers():
    interviewers = Interviewer.get_all()
    results = []

    for interviewer in interviewers:
        obj = {
            'id': interviewer.id,
            'name': interviewer.name,
            'department': interviewer.department
        }
        results.append(obj)
    return results


def list_interviewees():
    interviewees = Interviewee.get_all()
    results = []

    for interviewee in interviewees:
        obj = {
            'id': interviewee.id,
            'name': interviewee.name,
            'linked_ind': interviewee.linked_in,
            'email': interviewee.email
        }
        results.append(obj)
    return results


def list_interviews():
    interviews = Interview.get_all()
    results = []

    for interview in interviews:
        obj = {
            'id': interview.id,
            'interviewee': interview.interviewee,
            'interviewer': interview.interviewer,
            'start_time': interview.start_time,
            'end_time': interview.end_time
        }
        results.append(obj)
    return results
