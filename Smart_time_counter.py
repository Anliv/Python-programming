#!/usr/bin/env python
# coding: utf-8

# In[28]:


class Counter:
    def __init__(self, limit, initial = 0, min_digits = 1):
        self.limit = limit
        if initial < 0 or initial > self.limit-1:
            print('Error: Initial value out of bounds. Setting to limit instead.')
            initial = self.limit - 1
        self.value = initial
        self.min_digits = min_digits
    def get_value(self):
        return self.value
    def __str__(self):
        text = str(self.value)
        return text.zfill(self.min_digits)
    def tick(self):
        self.value -=1
        if self.value <0:
            self.value = self.limit - 1
            return True
        else:
            return False

counter1 = Counter(limit=10, initial=1, min_digits=5)
print(counter1.get_value())
counter1.tick()
print(counter1.get_value())
counter1.tick()
print(counter1.get_value())
print('Counter1 value as string:', str(counter1))

counter2 = Counter(limit=60, initial=1, min_digits=5)
print(counter2.get_value())
print()

            
test_counter = Counter(limit=10, initial=3, min_digits=5)
print(test_counter.get_value())
test_counter.tick()
print(test_counter.get_value())
test_counter.tick()
print(test_counter.get_value())
print('Counter value as string:', str(test_counter))


# In[41]:


class Timer:
    def __init__(self, hours, minutes, seconds):
        self.hours = Counter (limit=24, initial = hours, min_digits = 2)
        self.minutes = Counter (limit=60, initial = minutes, min_digits = 2)
        self.seconds = Counter (limit=60, initial = seconds, min_digits = 2)
        
    def __str__(self):
        return (str(self.hours)+":"+str(self.minutes)+":"+str(self.seconds))
    
    def tick(self):
        if self.seconds.tick():
            if self.minutes.tick():
                self.hours.tick()
        
        
    def is_zero(self):
        if self.tick() == "00:00:00":
            return True

            

print('Timer:')
test_timer = Timer(1,30,0)
print('Is zero:', test_timer.is_zero())
print(str(test_timer))
for i in range(60*90):
    test_timer.tick()
    print(str(test_timer))
print('Is zero:', test_timer.is_zero())


# In[ ]:




