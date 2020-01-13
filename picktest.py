from pick import pick

title = 'Please choose your required seat type: '
options = ['General seats', 'Restrictded seats']
selected = pick(options, title, multi_select=False, min_selection_count=1)
print (type(selected))
print (selected[0])