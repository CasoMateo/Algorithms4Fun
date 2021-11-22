import datetime

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

      date = datetime.datetime(year, month, day)
      days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
      
      return days[date.weekday()]
