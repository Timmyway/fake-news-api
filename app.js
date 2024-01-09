const apiRoutes = require('./routes/api');
const bodyParser = require('body-parser');

const app = express();

// Middlewares
app.use(bodyParser.urlencoded({extended: false}));
// Middleware to parse JSON
app.use(bodyParser.json());

app.use(apiRoutes);

app.listen(1337);