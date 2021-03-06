import pdb

# code to set up db
from models.location import Location
from models.trainer import Trainer
from models.member import Member
from models.fitness_class import FitnessClass
from models.attendance import Attendance

import repositories.location_repo as location_repo
import repositories.trainer_repo as trainer_repo
import repositories.member_repo as member_repo
import repositories.fitness_class_repo as fitness_class_repo
import repositories.attendance_repo as attendance_repo

location_repo.delete_all()
trainer_repo.delete_all()
member_repo.delete_all()
fitness_class_repo.delete_all()
attendance_repo.delete_all()


location1 = Location('Studio 1')
location_repo.save(location1)
location2 = Location('Studio 2')
location_repo.save(location2)
location3 = Location('Fitness Arena')
location_repo.save(location3)

trainer1 = Trainer('Zack', 'Black')
trainer_repo.save(trainer1)
trainer2 = Trainer('Kirsty', 'Whitehall')
trainer_repo.save(trainer2)
trainer3 = Trainer('Jamie', 'Gray')
trainer_repo.save(trainer3)

member1 = Member('Shaun', 'Hodge', 'standard', '2021/01/10', 'EH5 3RU', '07596685374', 'shaun.hodge@email.com')
member_repo.save(member1)
member2 = Member('Jade', 'Breslin', 'premium', '2020/08/13', 'EH12 1SU', '07759244212', 'jade.breslin@email.com')
member_repo.save(member2)
member3 = Member('Lucy', 'Atkinson', 'premium', '2019/10/25', 'EH2 6SR', '07321844372', 'lucy.atkinson@email.com')
member_repo.save(member3)
member4 = Member('James', 'Holden', 'standard', '2019/06/13', 'EH7 9DE', '07538472658', 'james.holden@email.com')
member_repo.save(member4)
member5 = Member('Gary', 'McDonald', 'standard', '2021/01/14', 'EH15 7ST', '07695844449', 'gary.mcdonals@email.com')
member_repo.save(member5)

fitness_class1 = FitnessClass('Body Attack', trainer2, location1, '2021/03/10', '13:00', 20)
fitness_class_repo.save(fitness_class1)
fitness_class2 = FitnessClass('HIIT', trainer1, location3, '2021/03/10', '17:00', 30)
fitness_class_repo.save(fitness_class2)
fitness_class3 = FitnessClass('Zumba', trainer1, location1, '2021/03/10', '18:15', 35)
fitness_class_repo.save(fitness_class3)
fitness_class4 = FitnessClass('Yoga', trainer2, location2, '2021/03/10', '07:00', 20)
fitness_class_repo.save(fitness_class4)

attendance1 = Attendance(fitness_class1, member2)
attendance_repo.save(attendance1)
attendance2 = Attendance(fitness_class1, member3)
attendance_repo.save(attendance2)
attendance3 = Attendance(fitness_class1, member4)
attendance_repo.save(attendance3)
attendance4 = Attendance(fitness_class2, member2)
attendance_repo.save(attendance4)
attendance5 = Attendance(fitness_class2, member3)
attendance_repo.save(attendance5)
attendance6 = Attendance(fitness_class3, member5)
attendance_repo.save(attendance6)
attendance7 = Attendance(fitness_class4, member2)
attendance_repo.save(attendance7)
attendance8 = Attendance(fitness_class4, member1)
attendance_repo.save(attendance8)

pdb.set_trace()