import web
from web import form
from web.contrib.template import render_jinja

# Database connection
db = web.database(dbn='postgres', user='rekah', pw='etwin', db='webpy_test')

view = render_jinja('views', encoding='utf-8')


class Add:
    def POST(self):
        i = web.input()
        db.insert('myuser', name=i.name, age=i.age, bio=i.bio, fav_food=i.fav_food)
        raise web.seeother('/users')


class Hello:
    def GET(self, name):
        users = db.select('myuser')
        context = {'name': name, 'users': users}
        return view.hello(context)


class Staff:
    def GET(self, id=None):
        staffs = db.select('staff')
        if id is None:
            context = {'staffs': staffs}
            return view.staff_list(context)
        else:
            vars = dict(id=id)
            results = db.select('staff', where="id=$id", vars=vars, _test=True)
            if results is not None:
                staff_result = db.query(results)
                for staff in staff_result:
                    return view.staff_detail({'staff': staff})
            raise web.seeother('/error')

    def POST(self, staff_id=None):
        if staff_id is None:
            i = web.input()
            # x = web.input(myfile={})
            names = i.names
            role = i.role
            print "names: %s, role: %s" % (names, role)
            db.insert('staff', names=names, role=role)
            raise web.seeother('/staff')
        else:
            x = web.input()
            names = x.names
            role = x.role
            vars = dict(staff_id=staff_id)
            results = db.update(
                'staff',
                where="id=$staff_id", 
                vars=vars, _test=True, 
                names=names, 
                role=role)
            updated_staff = db.query(results)
            raise web.seeother('/staff')
            

class Error:
    def GET(self):
        return view.error_no_results("")


class Success:
    def GET(self):
        return view.sucess("")


class DeleteStaff:
    def GET(self, id):
        vars = dict(id=id)
        result = db.delete('staff', where="id=$id", vars=vars, _test=True)
        deleted_staff = db.query(result)
        raise web.seeother('/staff')