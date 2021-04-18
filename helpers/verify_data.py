def verify_data(request):
    data = request.get_data()
    if len(data) == 0:
        return False
    return True
