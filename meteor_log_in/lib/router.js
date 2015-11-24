/**
 * Created by Kristian on 03/08/15.
 */

FlowRouter.route('/blog/:postId', {
    action: function (params, queryParams) {
        console.log("Yeah! We are on the post:", params.postId);
    }
});