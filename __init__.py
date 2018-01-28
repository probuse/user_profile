import web, app.controller

# Application urls
urls = (
    '/add', 'app.controller.Add',
    '/hello/(.*)', 'app.controller.Hello',
    '/staff', 'app.controller.Staff',
    '/staff/edit/([0-9]+)', 'app.controller.Staff',
    '/staff/delete/([0-9]+)', 'app.controller.DeleteStaff',
    '/error', 'app.controller.Error',
    '/success', 'app.controller.Success',

)


if __name__ == '__main__':
    app = web.application(urls)
    web.internalerror = web.debugerror
    app.run()

