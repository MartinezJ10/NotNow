<template>
  <Nav />
  <ListCategory />
</template>

<script>
import { defineAsyncComponent } from "vue";

const Nav = defineAsyncComponent(() =>
  import("@/components/Nav" /* webpackChunkName: "Nav" */)
);
const ListCategory = defineAsyncComponent(() =>
  import("@/components/ListCategory" /* webpackChunkName: "ListCategory" */)
);
export default {
  name: "Home",
  components: {
    Nav,
    ListCategory,
  },
};
</script>

<style></style>
