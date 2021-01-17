import { createRouter, createWebHistory } from "vue-router";

const Home = () => import("../views/Home.vue");
const Detail = () => import("../views/Detail.vue");
const Upload = () => import("../views/Upload.vue");
const Gallery = () => import("../views/Gallery.vue");
const CategoryFilter = () => import("../views/CategoryFilter.vue");

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/gallery",
    name: "Gallery",
    component: Gallery,
  },
  {
    path: "/upload",
    name: "Upload",
    component: Upload,
  },
  {
    path: "/details/:id",
    name: "Detail",
    component: Detail,
  },
  {
    path: "/category/:id",
    name: "CategoyFilter",
    component: CategoryFilter,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
