<template>
  <form class="form" @submit.prevent="onUpload()" method="POST">
    <div class="form-block">
      <label for="title">Title</label>
      <input class="input" type="text" v-model="state.post.title" />
    </div>
    <div class="form-block">
      <label for="description">Description</label>
      <textarea class="input" v-model="state.post.description"></textarea>
    </div>
    <div class="form-block">
      <label for="category">Category</label>
      <select class="input" v-model="state.post.category">
        <option
          v-for="option in state.optionValue"
          :key="option.id"
          :value="option.name"
          >{{ option.name }}</option
        >
      </select>
    </div>
    <div class="form-block">
      <label for="image">Image</label>
      <input
        style="display:none"
        type="file"
        ref="img"
        @change="onFileSelected($event)"
      />
      <a class="btn" @click="$refs.img.click()">Select Image +</a>
      <p v-if="state.post.myImage">
        {{ state.post.myImage.name }}
      </p>
    </div>
    <div class="form-block ">
      <button class="btn sub" type="submit">Submit</button>
    </div>
  </form>
</template>

<script>
import { getAPI } from "@/axios_api.js";
import { onMounted, reactive } from "vue";
import swal from "sweetalert";

export default {
  name: "Form",
  setup() {
    const state = reactive({
      optionValue: {},
      post: {
        title: "",
        description: "",
        category: "",
        myImage: null,
      },
    });

    const getCategory = async () => {
      try {
        const resp = await getAPI.get("/api/category/");
        state.optionValue = resp.data;
      } catch (err) {
        console.log(err);
      }
    };

    function onFileSelected(event) {
      state.post.myImage = event.target.files[0];
    }

    const onUpload = async () => {
      const fd = new FormData();
      fd.append("title", state.post.title);
      fd.append("alt", state.post.description);
      fd.append("category", state.post.category);
      fd.append("image", state.post.myImage);

      try {
        await getAPI.post("/api/images/", fd);
        swal("Post Created Succesfully!", {
          buttons: false,
          timer: 1500,
          icon: "success",
        });

        resetForm();
      } catch (err) {
        swal({
          buttons: false,
          title: "There is Something Wrong",
          text: "Make sure to check all the inputs information",
          timer: 2000,
          icon: "error",
        });
        console.log(err);
      }
    };
    function resetForm() {
      //Iterate through each object field, key is name of the object field`
      Object.keys(state.post).forEach(function(key) {
        state.post[key] = "";
      });
    }
    onMounted(() => {
      getCategory();
    });

    return {
      state,
      onFileSelected,
      onUpload,
    };
  },
};
</script>
