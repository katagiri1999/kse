import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('../views/index.vue')
  },
  {
    path: '/index.html',
    component: () => import('../views/index.vue')
  },
  {
    path: '/index_jpn.html',
    component: () => import('../views/index_jpn.vue')
  },
  {
    path: '/car.html',
    component: () => import('../views/car.vue')
  },
  {
    path: '/car_jpn.html',
    component: () => import('../views/car_jpn.vue')
  },
  {
    path: '/inquiry.html',
    component: () => import('../views/inquiry.vue')
  },
  {
    path: '/inquiry_jpn.html',
    component: () => import('../views/inquiry_jpn.vue')
  },
  {
    path: '/book.html',
    component: () => import('../views/book.vue')
  },
  {
    path: '/book_jpn.html',
    component: () => import('../views/book_jpn.vue')
  },
  {
    path: '/admin_jpn.html',
    component: () => import('../views/admin_jpn.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
