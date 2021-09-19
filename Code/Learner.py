{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import itertools\n",
    "import json\n",
    "\n",
    "states = []\n",
    "\n",
    "with open(\"qvalues.json\", \"w\") as f:\n",
    "\tjson.dump(states, f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "import itertools\n",
    "import random\n",
    "import json\n",
    "\n",
    "class Leaner(object):\n",
    "    def __init__(self, display_width, display_height, block_size):\n",
    "        # Game parameters\n",
    "        self.display_width = display_width\n",
    "        self.display_height = display_height\n",
    "        self.block_size = block_size\n",
    "\n",
    "        # Learning parameters\n",
    "        self.epsilon = 0.1\n",
    "        self.lr = 0.7\n",
    "        self.discount = 0.9\n",
    "\n",
    "        # State/Action history\n",
    "        self.qvalues = self.LoadQvalues()\n",
    "        self.history = []\n",
    "\n",
    "        # Action space\n",
    "        self.actions = {\n",
    "            0:'left',\n",
    "            1:'right',\n",
    "            2:'up',\n",
    "            3:'down'\n",
    "        }\n",
    "    \n",
    "    def Reset(self):\n",
    "        self.history = []\n",
    "        \n",
    "    def LoadQvalues(self, path=\"qvalues.json\"):\n",
    "        with open(path, \"r\") as f:\n",
    "            qvalues = json.load(f)\n",
    "        return qvalues\n",
    "\n",
    "    def SaveQvalues(self, path=\"qvalues.json\"):\n",
    "        with open(path, \"w\") as f:\n",
    "            json.dump(self.qvalues, f)\n",
    "            \n",
    "    def act(self, snake, food):\n",
    "        \n",
    "        self.state = (snake, food)\n",
    "        \n",
    "        #Epislon greedy\n",
    "        rand = random.uniform(0,1)\n",
    "        if rand < self.epsilon:\n",
    "            action_key = random.choices(list(self.actions.keys()))[0]\n",
    "        else:\n",
    "            if self.state not in list(self.qvalues):\n",
    "                self.qvalues[str(self.state)] = [0,0,0,0]\n",
    "                \n",
    "            state_scores = self.qvalues[str(self.state)]\n",
    "            action_key = state_scores.index(max(state_scores))\n",
    "        action_val = self.actions[action_key]\n",
    "       \n",
    "    # Remember the actions it took at each state\n",
    "        self.history.append({\n",
    "            'state': state,\n",
    "            'action': action_key\n",
    "            })\n",
    "        \n",
    "        return action_val\n",
    "    \n",
    "    def UpdateQValues(self, reason):\n",
    "        history = self.history[::-1]\n",
    "        for i, h in enumerate(history[:-1]):\n",
    "            if reason: # Snake Died -> Negative reward\n",
    "                sN = history[0]['state']\n",
    "                aN = history[0]['action']\n",
    "                state_str = str(self.sN)\n",
    "                reward = -1\n",
    "                self.qvalues[state_str][aN] = (1-self.lr) * self.qvalues[state_str][aN] + self.lr * reward # Bellman equation - there is no future state since game is over\n",
    "                reason = None\n",
    "            else:\n",
    "                s1 = h['state'] # current state\n",
    "                s0 = history[i+1]['state'] # previous state\n",
    "                a0 = history[i+1]['action'] # action taken at previous state\n",
    "                \n",
    "                if s0.food != s1.food: # Snake ate a food, positive reward\n",
    "                    reward = 1\n",
    "                else:\n",
    "                    reward = -1\n",
    "                    \n",
    "                state_str = str(self.s0)\n",
    "                new_state_str = str(self.s1)\n",
    "                self.qvalues[state_str][a0] = (1-self.lr) * (self.qvalues[state_str][a0]) + self.lr * (reward + self.discount*max(self.qvalues[new_state_str])) # Bellman equation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
