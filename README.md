# securitycam
DLNN based security camera tracks people and vehicles then logs counts from video feed.

System currently deploys ssd-mobilenet-v2 on NVidia hardware for real time inference.

| <a href="https://www.seagate.com/video-storage-calculator/" target="_blank">**Seagate Surveillance Storage Calculator**</a>


Storage media for surveillance footage is costly. Even with the advantage of .h265 compression 6 video feeds at only 20 frames per second and 1080p resolution will generate over 154 Gigabytes of media to be stored PER 24 hour cycle. 31 days of the same footage quickly climbs past 4.5 Tb. This is enough to fill a 30 Tb HP magnetic tape at a cost of $86 in 6 months, and we don't even have the best quality footage available today, far from it. Similarly, a $50 IBM LTO Ultrium 7 Tape would be full in 3 months. Worse the read speed of magnetic tapes leaves much to be desired, and they are not necessarily THE most reliable storage medium for critical data, merely a cost effective solution at scale. By comparison even a Seagate Skyhawk 4TB Surveillance SATA drive would cost $100 and would be filled with the previously described footage in 31 days.

In addition there is the problem of monitoring and auditing the footage. Historically a pair of human eyes was required to at least fast forward through hours if not days of footage of empty fields, rooms, halls, and parking lots to find a few moments of useful information. By using DLNNs we can edit out the empty footage in real time and archive only the footage that contains, for example, humans. In addition we can automatically generate searchable and sortable log data from these feeds enabling an auditor to search for an instance of a person on a given day, or at a certain time, and quickly find if that footage even exists, without the need to recover hours of archived video and scan through it minute by minute.

| <a href="https://github.com/dusty-nv/jetson-inference" target="_blank">Jetson AI HelloWorld Docker container series</a>
