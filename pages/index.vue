<template>
	<div>
		<div class="ui pointing menu">
			<a class="active item">
				Home
			</a>
			<a class="item">
				Messages
			</a>
			<a class="item">
				Friends
			</a>
			<div class="right menu">
				<div class="item">
				<div class="ui transparent icon input">
					<input type="text" placeholder="Search...">
					<i class="search link icon"></i>
				</div>
				</div>
			</div>
		</div>
		<div class="ui container">
			<h1>Handwriting Recognition</h1>
			<div class="ui segment">
				<div class="ui two column very relaxed grid">
					<div class="column">
						<no-ssr>
							<file-pond
								name="test"
								ref="pond1"
								label-idle="Drop files here..."
								allow-multiple="false"
								accepted-file-types="image/jpeg, image/png"
								v-bind:files="myFiles"
                            	v-on:processfile="addtopreview"
								v-on:addfile="fileadded"
								/>
						</no-ssr>
					</div>
					<div class="column">
						<p></p>
						<p></p>
						<p></p>
						<p></p>
					</div>
				</div>
				<div class="ui vertical divider">
					and
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import vueFilePond from 'vue-filepond';
import 'filepond/dist/filepond.min.css';
import 'filepond-plugin-image-preview/dist/filepond-plugin-image-preview.min.css';
import FilePondPluginFileValidateType from 'filepond-plugin-file-validate-type';
import FilePondPluginImagePreview from 'filepond-plugin-image-preview';
const FilePond = vueFilePond( FilePondPluginFileValidateType, FilePondPluginImagePreview );
export default {
	name: 'app',
    data: function() {
        return {
			myFiles: []
		};
    },
    components: {
        FilePond
    },
    methods: {
		addtopreview(error, file){
            // var p='<br><img style="max-width:100%;height:auto" src="'+file.serverId+'" /><br>'
            // this.content.text+= p
			// this.myFiles=[]
			console.log(file)
		},
		fileadded(error, file){
			console.log(file);
			
		}
    },
}
</script>

<style>

</style>
