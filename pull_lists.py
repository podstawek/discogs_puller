import discogs_client
import sys
from config import token, username

d = discogs_client.Client('ExampleApplication/0.1', user_token=token)
user = d.user(username)
lists = user.lists
howmanylists = lists.count
print ("There are " + str(howmanylists) + " lists.")
howmanypages = lists.pages
print ("There are " + str(howmanypages) + " pages of lists.")
firstpage = lists.page(0)
print ("The first page of lists has " + str(len(firstpage)) + " items.")

with open('index.html', 'w') as f:
    f.write('<htML> <head> <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/> <title>Best Music</title> <link rel="stylesheet" type="text/css" href="musicstyle.css" media="screen"/></head><body>')
    f.write('<h1>My Favorite Music</h1>')
    f.write('<p>Personal list of the best music albums. There is no specific order or ranking; if an album is on this list, it is in some way beautiful, and I listen to it again and again.</p>')
    f.write('<p>The list is built using Discogs API and based on my saved lists of albums at Discogs.</p>')

    list_of_lists = []
    for n in firstpage:
       list_of_lists.append(n) 

    for l in list_of_lists:
        f.write('<a href="#' + str(l.id) + '">' + d.list(l.id).name + '</a><br>')
    
    stopper = 0
    for n in list_of_lists:
        stopper += 1
        if stopper > 2:
            nop = None
        print (n.id)
        current_list = d.list(n.id)
        f.write('<h2 id="' + str(n.id) + '">' + current_list.name + '</h2>')
        #f.write('<table>')
        f.write('<main>')
        counter = 1
        for i in current_list.items:
            sys.stderr.write(str(counter) + ' ')
            sys.stderr.flush()
            counter+= 1
            try:
                master_data = d.master(i.data['id'])
                mr = master_data.main_release
                genres = master_data.genres
                genres_string = ''
                c = 0
                for g in genres:
                    if c == 0:
                        genres_string += g
                    else:
                        genres_string += (', ' + g)
                    c += 1
                styles = master_data.styles
                styles_string = ''
                c = 0
                if styles:
                    for g in styles:
                        if c == 0:
                            styles_string += g
                        else:
                            styles_string += (', ' + g)
                        c += 1
                else:
                    styles_string = ''
                artists = mr.artists
                artists_string = ''
                c = 0
                for g in artists:
                    #print (dir(g))
                    if c == 0:
                        artists_string += g.name
                    else:
                        artists_string += (', ' + g.name)
                    c += 1
                music_genre = genres_string + ('' if styles_string == '' else (' (' + styles_string + ')'))
                f.write('<section><table><tr>')
                f.write('<td><img src="' + i.data['image_url'] + '" width=100></td><td><a href="' + i.url + '">' + str(master_data.title) + '</a><br>' + artists_string + '<br>' + i.comment + '<br><span class="genre">' + music_genre + '</span><br></td></tr><tr><td class="year">' + str(master_data.year) + '</td><td class="country">' + mr.country + '</td></tr></table></section>') 
            except:
                f.write('<section><table><tr>')
                f.write('<td><img src="' + i.data['image_url'] + '" width=100></td><td><a href="' + i.url + '">' + i.display_title + '</a><br>' + 'n/a' + '<br>' + i.comment + '<br><span class="genre">' + 'n/a' + '</span><br></td></tr><tr><td class="year">' + 'n/a' + '</td><td class="country">' + 'n/a' + '</td></tr></table></section>') 



        f.write('</main>')


    f.write('</body>')
current_list = d.list(1351230)
print (dir(current_list))
print (dir(d.master(64167)))
print (d.master(64167).data)
print (d.master(64167).main_release)
print (dir(d.master(64167).main_release))
