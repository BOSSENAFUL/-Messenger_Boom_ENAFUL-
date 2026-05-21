const express = require('express');
const { exec } = require('child_process');
const path = require('path');
const app = express();

app.use(express.json());
app.use(express.static(path.join(__dirname))); // যাতে HTML ফাইলটি কাজ করে

// হোমপেজ লোড করার জন্য
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// বট ডিপ্লয় করার জন্য API
app.post('/deploy', (req, res) => {
    const { repoUrl } = req.body;
    if (!repoUrl) return res.status(400).send("GitHub Link missing!");

    console.log(`Deploying from: ${repoUrl}`);
    
    // নিরাপত্তার জন্য 'rm -rf' দিয়ে আগে পুরনো ফোল্ডার পরিষ্কার করে নেওয়া হচ্ছে
    exec(`mkdir -p ./bots && rm -rf ./bots/user_bot && git clone ${repoUrl} ./bots/user_bot`, (err, stdout, stderr) => {
        if (err) {
            console.error(err);
            return res.status(500).send("Deployment failed!");
        }
        res.send("Bot deployed successfully!");
    });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
