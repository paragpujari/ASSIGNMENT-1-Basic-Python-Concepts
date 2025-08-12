# # 2. Create a Personalized Greeting
# 
# ## Problem Statement: Write a Python program that:
# 
#  1.  Takes a user's first name and last name as input.
# 
#  2.  Concatenates the first name and last name into a full name.
# 
#  3.  Prints a personalized greeting message using the full name.
# 

# In[10]:


# Takes a user's first name and last name as input.

first_name = input('Enter your first name :')

last_name = input('Enter your last name :')

# Concatenates the first name and last name into a full name.

full_name = first_name + ' ' + last_name

print(full_name)


# Prints a personalized greeting message using the full name.

print('Hello, {0} {1}! Welcome to the Python program.'.format(first_name, last_name))
