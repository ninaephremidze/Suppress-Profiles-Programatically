# Suppress-Profiles-Programatically
This repo finds a specific segment you'd like to suppress and then calls the email members that are in that segment.
For example, let's say your customer has a list with @amazon.com emails that they want to suppress.
In that case, you'd create a segment and then suppress them programatically.

This script consists of two primary steps:
a) API Endpoint: Get Segment. Make sure to specify the segment ID you are trying to get
b) Once you get a success message in part a, suppress the segment by using suppress API endpoint

