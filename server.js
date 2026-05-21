const express = require('express');
const cors = require('cors'); // CORS সাপোর্ট যোগ করা হয়েছে
const { exec } = require('child_process');
const path = require('path');
const app = express();

// Middleware
app.use(cors()); // যেকোনো ডোমেইন থেকে রিকোয়েস্ট এলাও করার জন্য
app.use(express.json());
app.use(express.static(path.join(__dirname))); // স্ট্যাটিক ফাইল বা index.html দেখানোর জন্য

// হোমপেজ লোড করার জন্য
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// বট ডিপ্লয় করার জন্য API
app.post('/deploy', (req, res) => {
    const { repoUrl } = req.body;
    if (!repoUrl) return res.status(400).send("GitHub Link missing!");

    console.log(`Deploying from: ${repoUrl}`);
    
    // ডিপ্লয়মেন্ট লজিক
    exec(`mkdir -p ./bots && rm -rf ./bots/user_bot && git clone ${repoUrl} ./bots/user_bot`, (err, stdout, stderr) => {
        if (err) {
            console.error(err);
            return res.status(500).send("Deployment failed!");
        }
        res.send("Bot deployed successfully!");
    });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Hosting Server running on port ${PORT}`));
