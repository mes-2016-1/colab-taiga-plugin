
def logout_user(sender, user, request, **kwargs):
    print(request.session)
    request.session.clear()
    
