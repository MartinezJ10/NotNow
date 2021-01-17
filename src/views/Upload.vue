<template>
  <Nav />
  <Form />
</template>

<script>
import { defineAsyncComponent } from "vue";

const Form = defineAsyncComponent(() =>
  import("@/components/Form" /* webpackChunkName: "Form" */)
);
const Nav = defineAsyncComponent(() =>
  import("@/components/Nav" /* webpackChunkName: "Nav" */)
);

export default {
  name: "Upload",
  components: {
    Nav,
    Form,
  },
};
</script>

<style></style>
