import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import components from '@/components/UI'

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://127.0.0.1:8000'  // FastAPI backend

const app = createApp(App)

components.forEach(component => 
    {
        app.component(component.name, component)
    }
)

app.use(store).use(router).mount('#app')
