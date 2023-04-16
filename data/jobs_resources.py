from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource

from data import db_session
from data.jobs import Jobs

app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('team_leader', required=True)
parser.add_argument('job', required=True)
parser.add_argument('work_size', required=True)
parser.add_argument('collaborators', required=True)
parser.add_argument('start_date', required=True)
parser.add_argument('end_date', required=True)
parser.add_argument('is_finished', required=True)


def abort_if_jobs_not_found(job_id):
    session = db_session.create_session()
    user = session.query(Jobs).get(job_id)
    if not user:
        abort(404, message=f"Job {job_id} not found")


class JobResource(Resource):
    def get(self, job_id):
        abort_if_jobs_not_found(job_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(job_id)
        return jsonify({'User': jobs.to_dict(
            only=('team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished', 'id'))})

    def delete(self, job_id):
        abort_if_jobs_not_found(job_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(job_id)
        session.delete(jobs)
        session.commit()
        return jsonify({'success': 'OK'})


class JobListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'Jobs': [item.to_dict(
            only=('job', 'team_leader', 'is_finished')) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        jobs = Jobs(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            start_date=args['start_date'],
            end_date=args['end_date'],
            is_finished=args['is_finished']
        )
        session.add(jobs)
        session.commit()
        return jsonify({'success': 'OK'})