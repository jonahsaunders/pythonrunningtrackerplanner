from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import math

currentday = 1
activeday = 1
curmileage = 0
curdescription = ""

maxmileage = 10

curCycle = 1
curWeek = 1

goodpain = 0
badpain = 0

race = 0
#0 is mile, 1 is 5k, 2 is 10k, 3 is HM, 4 is M

runs = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: '', 15: '', 16: '', 17: '', 18: '', 19: '', 20: '', 21: '', 22: '', 23: '', 24: '', 25: '', 26: '', 27: '', 28: '', 29: '', 30: '', 31: '', 32: '', 33: '', 34: '', 35: '', 36: '', 37: '', 38: '', 39: '', 40: '', 41: '', 42: '', 43: '', 44: '', 45: '', 46: '', 47: '', 48: '', 49: '', 50: '', 51: '', 52: '', 53: '', 54: '', 55: '', 56: '', 57: '', 58: '', 59: '', 60: '', 61: '', 62: '', 63: '', 64: '', 65: '', 66: '', 67: '', 68: '', 69: '', 70: '', 71: '', 72: '', 73: '', 74: '', 75: '', 76: '', 77: '', 78: '', 79: '', 80: '', 81: '', 82: '', 83: '', 84: ''}

goodpainarray = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: '', 15: '', 16: '', 17: '', 18: '', 19: '', 20: '', 21: '', 22: '', 23: '', 24: '', 25: '', 26: '', 27: '', 28: '', 29: '', 30: '', 31: '', 32: '', 33: '', 34: '', 35: '', 36: '', 37: '', 38: '', 39: '', 40: '', 41: '', 42: '', 43: '', 44: '', 45: '', 46: '', 47: '', 48: '', 49: '', 50: '', 51: '', 52: '', 53: '', 54: '', 55: '', 56: '', 57: '', 58: '', 59: '', 60: '', 61: '', 62: '', 63: '', 64: '', 65: '', 66: '', 67: '', 68: '', 69: '', 70: '', 71: '', 72: '', 73: '', 74: '', 75: '', 76: '', 77: '', 78: '', 79: '', 80: '', 81: '', 82: '', 83: '', 84: ''}
badpainarray = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: '', 15: '', 16: '', 17: '', 18: '', 19: '', 20: '', 21: '', 22: '', 23: '', 24: '', 25: '', 26: '', 27: '', 28: '', 29: '', 30: '', 31: '', 32: '', 33: '', 34: '', 35: '', 36: '', 37: '', 38: '', 39: '', 40: '', 41: '', 42: '', 43: '', 44: '', 45: '', 46: '', 47: '', 48: '', 49: '', 50: '', 51: '', 52: '', 53: '', 54: '', 55: '', 56: '', 57: '', 58: '', 59: '', 60: '', 61: '', 62: '', 63: '', 64: '', 65: '', 66: '', 67: '', 68: '', 69: '', 70: '', 71: '', 72: '', 73: '', 74: '', 75: '', 76: '', 77: '', 78: '', 79: '', 80: '', 81: '', 82: '', 83: '', 84: ''}


milePercents = {1: .1, 2: .1875, 3: .1, 4: .17, 5: .11, 6: .08, 7: .26, 8: .1, 9: .1875, 10: .1, 11: .17, 12: .11, 13: .08, 14: .26, 15: .1, 16: .1875, 17: .1, 18: .17, 19: .11, 20: .08, 21: .26, 22: .1, 23: .1875, 24: .1, 25: .17, 26: .11, 27: .08, 28: .26, 29: .1, 30: .1875, 31: .1, 32: .17, 33: .11, 34: .08, 35: .26, 36: .1, 37: .1875, 38: .1, 39: .17, 40: .11, 41: .08, 42: .26, 43: .1, 44: .1875, 45: .1, 46: .17, 47: .11, 48: .08, 49: .26, 50: .1, 51: .1875, 52: .1, 53: .17, 54: .11, 55: .08, 56: .26, 57: .1, 58: .1875, 59: .1, 60: .17, 61: .11, 62: .08, 63: .26, 64: .1, 65: .1875, 66: .1, 67: .17, 68: .11, 69: .08, 70: .26, 71: .1, 72: .1875, 73: .1, 74: .17, 75: .11, 76: .08, 77: .26, 78: .1, 79: .1875, 80: .1, 81: .17, 82: .11, 83: .08, 84: .26}
mileTotalPercents = {1: .7376, 2: .7789, 3: .8316, 4: .8632, 5: .6737, 6: .8632, 7: .9053, 8: .9474, 9: 1, 10: 1, 11: .8842, 12: .65}
mileWorks = {1: "Workout #1: 16 mins @ tempo    Workout #2: 3x1200m @ 5K", 2: "Workout #1: 16 mins @ tempo    Workout #2: 3x1200m @ 5K", 3: "Workout #1: 20 mins @ tempo    Workout #2: 4x1200m @ 5K", 4: "Workout #1: 20 mins @ tempo    Workout #2: 4x1200m @ 5K", 5: "Workout #1: 25 mins @ tempo    Workout #2: 5x1000m @ 5K", 6: "Workout #1: 25 mins @ tempo    Workout #2: 5x1000m @ 5K", 7: "Workout #1: 6x1000 @ 5K (2')   Workout #2: 3x4x400 @ 3s/lap faster than 5K (200m/400m)", 8: "Workout #1: 6x1000 @ 5K (2')   Workout #2: 2x6x400 @ 3K (200m/400m)", 9: "Workout #1: 6x800 @ 4s/lap slower than 3K    Workout #2: 2x4x200 @ mile (200m/400m)", 10: "Workout #1: 8x400 @ mile (2')     Workout #2: 6x150 @ 90-95% (3-5')", 11: "Workout #1: 6x400 @ mile (2')     Workout #2: 2x4x200 @ mile (200m/400m)", 12: "Workout #1: 800m @ mile, 4x200 @ mile     Workout #2: Mile Race"}

class Home(Screen):
    def maxmileageinput(self, mileagevalue):
        global maxmileage
        try:
            maxmileage = float(mileagevalue)
            self.ids.maxmileagetext.text = "Max Mileage: " + str(maxmileage)

            calendar = self.manager.get_screen('calendar')
            for i in range(1, 29):
                weekIndexGetValue = (math.ceil(i / 7) + (4 * (curCycle - 1)))
                dailyIndexGetValue = i + (28 * (curCycle - 1))
                dailyMileagePercent = milePercents.get(dailyIndexGetValue)
                weeklyMileagePercent = mileTotalPercents.get(weekIndexGetValue)
                curIndexInfo = round((weeklyMileagePercent * dailyMileagePercent * float(mileagevalue)), 1)
                toString = str(i + (28 * (curCycle - 1)) - 28 * (curCycle) + 28)
                label = "goalmileage" + toString
                calendar.ids[label].text = str(curIndexInfo) + " miles"



        except:
            self.ids.maxmileagetext.text = "Please input a number"



    def setGoodPain(self, painvalue):
        global goodpainarray
        global goodpain
        global currentday
        calendar = self.manager.get_screen('calendar')
        goodpain = painvalue
        goodpainarray[activeday] = painvalue
        self.ids.curGoodPain.text = str(painvalue)
        calendar.ids.goodpaincal.text = str(goodpain) + " good pain"

    def getGoodPain(self):
        return goodpain

    def setBadPain(self, painvalue):
        global badpainarray
        global badpain
        global currentday
        calendar = self.manager.get_screen('calendar')
        badpain = painvalue
        badpainarray[activeday] = painvalue
        self.ids.curBadPain.text = str(painvalue)
        calendar.ids.badpaincal.text = str(badpain) + " bad pain"

    def getBadPain(self):
        return badpain

    def setRace(self, racevalue):
        global race
        race = racevalue
        label = ""
        if race == 0:
            label = "Mile"
        if race == 1:
            label = "5k"
        if race == 2:
            label = "10k"
        if race == 3:
            label = "Half marathon"
        if race == 4:
            label = "Marathon"
        self.ids.currace.text = label


class TrainingPlan(Screen):

    def setDay(self, dayvalue):
        global currentday
        global activeday
        global badpainarray
        global goodpainarray
        currentday = dayvalue
        self.ids.activeday.text = "Day: " + str(dayvalue)
        home = self.manager.get_screen('home')
        calendar = self.manager.get_screen('calendar')
        home.ids.currentDayHome.text = "Selected Day: " + str(dayvalue)
        activeday = currentday + (7 * (curWeek-1))
        calendar.ids.activedaycalendar.text = "Active Day: " + str(activeday)



    def getDay(self):
        return currentday

    def mileageinput(self, mileagevalue):
        global curmileage
        global runs
        try:
            curmileage = float(mileagevalue)
            runs[activeday] = curmileage
            calendar = self.manager.get_screen('calendar')

            if curCycle == 1 and activeday > 0 and activeday <= 28:
                firstlabel = "mileagerun"+str(activeday)
                calendar.ids[firstlabel].text = str(curmileage) + " miles"
            if curCycle == 2 and activeday > 28 and activeday <= 56:
                secondlabel = "mileagerun"+str(activeday-28)
                calendar.ids[secondlabel].text = str(curmileage) + " miles"
            if curCycle == 3 and activeday > 56 and activeday <= 84:
                thirdlabel = "mileagerun"+str(activeday-56)
                calendar.ids[thirdlabel].text = str(curmileage) + " miles"

        except:
            curmileage = 0


    def descriptioninput(self, description):
        curdescription = description

class Calendar(Screen):

    def increasecurrentcycle(self):
        global curCycle
        global runs
        global maxmileage
        maxCycle = 3
        minCycle = 1
        if curCycle < maxCycle:
            curCycle += 1
            self.ids.cycleof.text = "Cycle: " + str(curCycle) + "/3"
        #also update the week total miles


        calendar = self.manager.get_screen('calendar')
        for i in range(1, 29):
            curIndexInfo = runs.get(i+(28*(curCycle-1)))
            toString = str(i+(28*(curCycle-1)) - 28 * (curCycle) + 28)
            label = "mileagerun" + toString
            calendar.ids[label].text = str(curIndexInfo) + " miles"

        for i in range(1, 29):
            weekIndexGetValue = (math.ceil(i/7) + (4 * (curCycle-1)))
            dailyIndexGetValue = i + (28 * (curCycle - 1))
            dailyMileagePercent = milePercents.get(dailyIndexGetValue)
            weeklyMileagePercent = mileTotalPercents.get(weekIndexGetValue)
            curIndexInfo = round((weeklyMileagePercent * dailyMileagePercent * float(maxmileage)), 1)
            toString = str(i + (28 * (curCycle - 1)) - 28 * (curCycle) + 28)
            label = "goalmileage" + toString
            calendar.ids[label].text = str(curIndexInfo) + " miles"

    def decreasecurrentcycle(self):
        global curCycle
        global maxmileage
        maxCycle = 3
        minCycle = 1
        if curCycle > minCycle:
            curCycle -= 1
            self.ids.cycleof.text = "Cycle: " + str(curCycle) + "/3"
        #also update the week total miles
        calendar = self.manager.get_screen('calendar')
        for i in range(1, 29):
            curIndexInfo = runs.get(i+(28*(curCycle-1)))
            toString = str(i+(28*(curCycle-1)) - 28 * (curCycle) + 28)
            label = "mileagerun" + toString
            calendar.ids[label].text = str(curIndexInfo) + " miles"

        for i in range(1, 29):
            weekIndexGetValue = (math.ceil(i/7) + (4 * (curCycle-1)))
            dailyIndexGetValue = i + (28 * (curCycle - 1))
            dailyMileagePercent = milePercents.get(dailyIndexGetValue)
            weeklyMileagePercent = mileTotalPercents.get(weekIndexGetValue)
            curIndexInfo = round((weeklyMileagePercent * dailyMileagePercent * float(maxmileage)), 1)
            toString = str(i + (28 * (curCycle - 1)) - 28 * (curCycle) + 28)
            label = "goalmileage" + toString
            calendar.ids[label].text = str(curIndexInfo) + " miles"

    def setweek(self, toset):
        global curCycle
        global curWeek

        curWeek = toset + 4 * (curCycle-1)
        self.ids.activeweekcalendar.text = "Active Week: " + str(curWeek)
        self.ids.workout.text = mileWorks.get(curWeek)


    #glitching happening with this function. Too tired to fix
    def setdaycalendar(self, toset):
        global currentday
        global activeday
        global badpainarray
        global goodpainarray
        currentday = toset
        home = self.manager.get_screen('home')
        calendar = self.manager.get_screen('calendar')
        trainingplan = self.manager.get_screen('trainingplan')
        home.ids.currentDayHome.text = "Selected Day: " + str(toset)
        activeday = currentday + (7 * (curWeek-1))
        calendar.ids.activedaycalendar.text = "Active Day: " + str(activeday)
        trainingplan.ids.activeday.text = "Day: " + str(toset)
        currentpainbad = badpainarray.get(activeday)
        calendar.ids.badpaincal.text = str(currentpainbad) + " bad pain"
        currentpaingood = goodpainarray.get(activeday)
        calendar.ids.goodpaincal.text = str(currentpaingood) + " good pain"



class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("runningapp.kv")

#pos_hint is better
class RunningApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    RunningApp().run()

