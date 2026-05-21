const express = require('express');
const { exec } = require('child_process');
const app = express();

app.use(express.json());

// ইউজার যখন তাদের রিপোজিটরি লিংক দেবে
app.post('/deploy', (req, res) => {
    const { repoUrl } = req.body;
    
    // এখানে GitHub API বা Actions ট্রিগার করার লজিক থাকবে
    console.log(`Deploying bot from: ${repoUrl}`);
    
    exec(`git clone ${repoUrl} ./bots/user_bot`, (err, stdout, stderr) => {
        if (err) return res.status(500).send("Deployment failed!");
        res.send("Bot deployed successfully!");
    });
});

app.listen(3000, () => console.log('Hosting Server running on port 3000'));
