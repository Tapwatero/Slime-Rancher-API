import json
from flask import Flask
from flask_restful import Api, Resource, abort

app = Flask(__name__)
api = Api(app)

p = open("plorts.json")
plorts = json.load(p)

s = open("slimes.json")
slimes = json.load(s)


def abort_if_plort_invalid(plort):
    if plort not in plorts:
        abort(404, message="Plort Unfindable.")


def abort_if_slime_invalid(slime):
    if slime not in slimes:
        abort(404, message="Slime Unfindable.")


class Plorts(Resource):
    def get(self, plort):
        abort_if_plort_invalid(plort)
        return plorts[plort], 200


class Slimes(Resource):
    def get(self, slime):
        abort_if_slime_invalid(slime)
        return slimes[slime], 200


api.add_resource(Plorts, "/plorts/<string:plort>")
api.add_resource(Slimes, "/slimes/<string:slime>")

if __name__ == "__main__":
    app.run(debug=True)
