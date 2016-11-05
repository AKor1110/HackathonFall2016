#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class Tours(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('campus_tour.html')
		self.response.write(template.render())

class StudentCenter(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('student_center.html')
		self.response.write(template.render())

class Starbucks(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('starbucks.html')
		self.response.write(template.render())

class ResidentialHousingAssociation(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('packages.html')
		self.response.write(template.render())

class OtterCycleCenter(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('bikes.html')
		self.response.write(template.render())

class OC3(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('oc3.html')
		self.response.write(template.render())

class GreekLife(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('mgc.html')
		self.response.write(template.render())

class AssociatedStudents(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('as.html')
		self.response.write(template.render())

class StudentCentertoChapman(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('chapmancenter.html')
		self.response.write(template.render())

class ChapmanScienceCenter(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('chapman_center.html')
		self.response.write(template.render())

class ChapmanScienceCentertoWorldLanguageCenter(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('csc_to_wlc.html')
		self.response.write(template.render())

class WorldLanguageCenter(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('world_language_center.html')
		self.response.write(template.render())

class WorldLanguageCentertoStudentServices(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('studentservices.html')
		self.response.write(template.render())

class StudentServices(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('student_services.html')
		self.response.write(template.render())

class StudentServicestoUniversityCenter(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('universitycenter.html')
		self.response.write(template.render())

class UniversityCenter(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('university_center.html')
		self.response.write(template.render())

class Montes(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('montes.html')
		self.response.write(template.render())

class UniversityCentertoWorldTheater(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('worldtheater.html')
		self.response.write(template.render())

class WorldTheater(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('world_theater.html')
		self.response.write(template.render())

class WorldTheatertoLibrary(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('lib.html')
		self.response.write(template.render())

class Library(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('library.html')
		self.response.write(template.render())

class Peets(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('peets.html')
		self.response.write(template.render())

class CooperativeLearningCenter(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('tutors.html')
		self.response.write(template.render())

class LibrarytoBIT(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('libtobit.html')
		self.response.write(template.render())

class BluePole(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('emergency.html')
		self.response.write(template.render())

class BusinessInformationandTechnology(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('bit.html')
		self.response.write(template.render())

class GameResearchLab(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('games.html')
		self.response.write(template.render())

class BITtoManzanita(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('manzanita.html')
		self.response.write(template.render())

class Manzanita(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('dorms.html')
		self.response.write(template.render())

class ManzanitatoOEandDC(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('oeanddc.html')
		self.response.write(template.render())

class OtterExpressandDiningCommons(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('food.html')
		self.response.write(template.render())

class OEandDCtoGym(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('foodtogym.html')
		self.response.write(template.render())

class OtterSportsComplex(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('gym.html')
		self.response.write(template.render())

class DiskGolf(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('diskgolf.html')
		self.response.write(template.render())

class GymtoUPD(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('gymtoupd.html')
		self.response.write(template.render())

class UniversityPoliceDepartment(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('upd.html')
		self.response.write(template.render())

class UPDtoHealthCenter(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('healthcenter.html')
		self.response.write(template.render())

class HealthCenter(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('health_center.html')
		self.response.write(template.render())

class HealthCentertoBusStop(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('health_center_to_bus_stop.html')
		self.response.write(template.render())

class BusStop(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('bus.html')
		self.response.write(template.render())

class BusToStudentCenter(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('bus_to_student_center.html')
		self.response.write(template.render())

class Congratulations(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('end_of_tour.html')
		self.response.write(template.render())

class Attractions(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('attractions.html')
		self.response.write(template.render())

class Highway(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('highway.html')
		self.response.write(template.render())

class Beach(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('beach.html')
		self.response.write(template.render())

class CanneryRow(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('cannery_row.html')
		self.response.write(template.render())

class Target(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('target.html')
		self.response.write(template.render())

class Wharf(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('wharf.html')
		self.response.write(template.render())

class NoodleBar(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('noodle_bar.html')
		self.response.write(template.render())

class DelMonte(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('del_monte.html')
		self.response.write(template.render())

class CarmelPlaza(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('carmel_plaza.html')
		self.response.write(template.render())

class FordOrdTrails(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('fort_ord_trails.html')
		self.response.write(template.render())

class SeventeenMileDrive(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('seventeen_mile_drive.html')
		self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/campus_tour', Tours),
    ('/student_center', StudentCenter),
    ('/starbucks', Starbucks),
    ('/student_housing', ResidentialHousingAssociation),
    ('/otter_cycle_center', OtterCycleCenter),
    ('/oc3', OC3),
    ('/multicultural_greek_council', GreekLife),
    ('/associated_students', AssociatedStudents),
    ('/student_center_to_chapman', StudentCentertoChapman),
    ('/chapman_science_center', ChapmanScienceCenter),
    ('/chapman_to_world_language_center', ChapmanScienceCentertoWorldLanguageCenter),
    ('/world_language_center', WorldLanguageCenter),
    ('/world_language_center_to_student_services', WorldLanguageCentertoStudentServices),
    ('/student_services', StudentServices),
    ('/student_services_to_university_center', StudentServicestoUniversityCenter),
    ('/university_center', UniversityCenter),
    ('/university_center_to_world_theater', UniversityCentertoWorldTheater),
    ('/world_theater', WorldTheater),
    ('/world_theater_to_library', WorldTheatertoLibrary),
    ('/library', Library),
    ('/peets', Peets),
    ('/cooperative_learning_center', CooperativeLearningCenter),
    ('/library_to_bit', LibrarytoBIT),
    ('/blue_pole', BluePole),
    ('/business_information_and_technology', BusinessInformationandTechnology),
    ('/game_research_lab', GameResearchLab),
    ('/bit_to_manzanita', BITtoManzanita),
    ('/manzanita', Manzanita),
    ('/manzanita_to_oe_and_dc', ManzanitatoOEandDC),
    ('/otter_express_and_dining_commons', OtterExpressandDiningCommons),
    ('/oe_and_dc_to_gym', OEandDCtoGym),
    ('/otter_sports_complex', OtterSportsComplex),
    ('/disk_golf', DiskGolf),
    ('/gym_to_upd', GymtoUPD),
    ('/university_police_department', UniversityPoliceDepartment),
    ('/upd_to_health_center', UPDtoHealthCenter),
    ('/health_center', HealthCenter),
    ('/health_center_to_bus_stop', HealthCentertoBusStop),
    ('/bus_stop', BusStop),
    ('/bus_to_student_center', BusToStudentCenter),
    ('/end_of_tour', Congratulations),
    ('/attractions', Attractions),
    ('/highway', Highway),
    ('/beach', Beach),
    ('/cannery_row', CanneryRow),
    ('/target', Target),
    ('/wharf', Wharf),
    ('/noodle_bar', NoodleBar),
    ('/del_monte', DelMonte),
    ('/carmel_plaza', CarmelPlaza),
    ('/ford_ord_trails', FordOrdTrails),
    ('/seventeen_mile_drive', SeventeenMileDrive)

], debug=True)