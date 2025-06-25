IN ENGLISH:
1️⃣ ROS2 says: “Robot, please move forward 0.5 m/s” → sends /cmd_vel

2️⃣ Your node sends position/speed commands to Kangaroo → motors turn

3️⃣ At same time, your node asks Kangaroo:

"Hey Kangaroo — where are you now?"
Kangaroo says: "I'm at 125000 ticks" → your node calculates: "Ah, that means I’ve moved 1.2 meters forward."

4️⃣ Your node publishes this as /odom and TF.



what i need to do:
ITERATIVE PLAN:
✅ Step 1: Open serial, query Kangaroo for encoder position
✅ Step 2: Convert ticks to meters
✅ Step 3: Publish /odom
✅ Step 4: Publish TF
✅ Step 5: Tune, test in RViz + Nav2