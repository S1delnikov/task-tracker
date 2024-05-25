import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import components from '@/components/UI'
import { VueMasonryPlugin } from 'vue-masonry'

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://127.0.0.1:8000'  // FastAPI backend
// axios.defaults.baseURL = 'https://task-tracker-5t53.onrender.com'

const app = createApp(App)

components.forEach(component => 
    {
        app.component(component.name, component)
    }
)

app.use(store).use(router).use(VueMasonryPlugin).mount('#app')
