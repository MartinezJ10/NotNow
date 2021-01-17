<template>
  <div class="nav">
    <div class="left">
      <router-link to="/">
        <h3>@NotNow</h3>
      </router-link>
    </div>
    <div class="right">
      <router-link class="link" :to="{ name: 'Gallery' }">Gallery</router-link>
      <router-link class="link" :to="{ name: 'Upload' }">Upload</router-link>
      <div>
        <label class="theme-switch" for="checkbox">
          <input
            type="checkbox"
            @change="toggleMode()"
            class="theme-switch"
            v-model="state.dark"
            id="checkbox"
          />
          <div class="slider round"></div>
        </label>
      </div>
    </div>
  </div>
</template>

<script>
import { onMounted, reactive } from "vue";

export default {
  name: "Nav",
  setup() {
    const state = reactive({
      dark: false,
    });

    function setTheme() {
      const currentTheme = localStorage.getItem("theme")
        ? localStorage.getItem("theme")
        : null;

      if (currentTheme) {
        document.documentElement.setAttribute("data-theme", currentTheme);

        if (currentTheme === "dark") {
          state.dark = true;
        }
      }
    }
    onMounted(() => {
      let bodyElement = document.body;
      bodyElement.classList.add("app-background");
      setTheme();
    });
    function toggleMode() {
      if (state.dark) {
        document.documentElement.setAttribute("data-theme", "dark");
        localStorage.setItem("theme", "dark");
      } else {
        document.documentElement.setAttribute("data-theme", "light");
        localStorage.setItem("theme", "light");
      }
    }

    return {
      toggleMode,
      state,
    };
  },
};
</script>
