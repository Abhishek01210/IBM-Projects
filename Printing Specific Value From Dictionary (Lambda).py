l=[{'make':'Nokia','model':216,'color':'black'},{'make':'Mi Max','model':2,'color':'Gold'},{'make':'Samsung','model':7,'color':'Blue'}]
z=filter(lambda x:x['model']>7,l)
print(list(z))