# What we do in this Section:
# Session
# Temporary Persistent Data
# 
# Module content:
# What are 'Session'?
# Using Session

# Here from what we done Last Day all work there Copy here.

# Firstly goto in reviews app in template review_detail.html page see there we add new button called Favorite.
# If i click on that button then from now that opened review my favorite and whichever existing favorite is now as normal review.


# What are Session?
# A session is 'ongoing connection' between a client (browser) and server.(Ongoing means even if browser is close or computer is shut down)
# It can be cleared, delete and reset.
# And devloper can deside how long it can be live.
# Data stored in a session persists as long as the session is active.
# So;
# In between client and Server, Server stores session_data + unique_identifier AND other side client store cookie which inside has session_id.(For info. session_data store in DB)



# First of all in settings.py MIDDLEWARE list 'django.contrib.sessions.middleware.SessionMiddleware', is added.
# Also in INSTALLED_APPS list 'django.contrib.sessions', is there.
# Also we add new variable SESSION_COOKIE_AGE to set age of cookie


# When we first time try storing session get error like: Object of type ReviewModel is not JSON serializable
# It generate because we try to store Object insted we now need to try to store string or dictionary.
# here we store full review in sesion that's why error is generate insted now we just store id of review. 