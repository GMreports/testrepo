alien_0 = {'color': 'green', 'points':5}


new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)



alien_0 = {'color': 'green'}

print("The alien is " + alien_0['color'] + ".") #forma mas conocida
print("The alien is {}.".format(alien_0['color'])) #usando .format
print(f"The alien is {alien_0['color']}.") #python 3.6 en adelante

alien_0['color2'] = "yellow"

print("The other alien is "+alien_0['color2'] + ".")
print("The other alien is {}.".format(alien_0['color2']))
print(f"The other alien is {alien_0['color2']}.")

alien_0 = {'color': 'red'}

print('Now the alien is color '+ alien_0['color'] + '.')
print("Now the alien is color {}.".format(alien_0['color']))
print(f"Now the alien is color {alien_0['color']}.")

#exercise

alien_0 = {'x_position':0, 'y_position':25, 'speed':'medium'}
print(f"Original x-position: {alien_0['x_position']}.")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else: 
    #this must be a fast alien
    x_increment = 3

#the new position is the old position plus the increment

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New x-position: {alien_0['x_position']}")

print("New x-position: {}".format(alien_0['x_position']))


alien_0 = {'color':'green', 'points':0}
print(f"{alien_0}")

del alien_0['points']
print(f"{alien_0}")

favorite_languages = {
    'jen':'Python',
    'Sarah':'C',
    'Edward':'Ruby',
    'Phil':'Python',
    }


print(f"Sarah's favorite language is {favorite_languages['Sarah']}")