# Split the mbid-unit-lesson-activity-frame

x = "8515-04-04-05-01"

mbid, unit, lesson, activity, frame = x.split('-')

print(f"mbid: {mbid}\nunit: {unit}\nlesson: {lesson}\nactivity: {activity}\nframe: {frame}")