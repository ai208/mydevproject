from . import models
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.utils.timezone import localtime
from .forms import HealthcareForm
from django.contrib.messages.views import SuccessMessageMixin
import io
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'IPAexGothic'
from django.shortcuts import render
from django.views import View

# Create your views here.
class HealthcareListView(ListView):
    model = models.Healthcare
    template_name = 'weightapp_cbv/healthcare_list.html'
    context_object_name='healthcares'

class HealthcareDetailView(DetailView):
    model = models.Healthcare
    template_name = 'weightapp_cbv/healthcare_detail.html'
    context_object_name='healthcare'

class HealthcareCreateView(SuccessMessageMixin,CreateView):
    model = models.Healthcare
    template_name = 'weightapp_cbv/healthcare_create.html'
    # fields = [    'physical_health','mental_health','eat_three_meals','exercise_time','sleep_time','weight','memo']
    form_class = HealthcareForm
    success_url = reverse_lazy('healthcare_list')
    success_message = '記録が「登録」されました。'

class HealthcareUpdateView(SuccessMessageMixin,UpdateView):
    model = models.Healthcare
    template_name = 'weightapp_cbv/healthcare_update.html'
    # fields = [    'physical_health','mental_health','eat_three_meals','exercise_time','sleep_time','weight','memo']
    form_class = HealthcareForm
    success_url = reverse_lazy('healthcare_list')
    success_message = '記録が「更新」されました。'
    def form_valid(self, form):
        healthcare = form.save()
        print(f"記録日:'{healthcare.created}' 更新日:'{healthcare.updated}'")
        return super().form_valid(form)

class HealthcareDeleteView(SuccessMessageMixin,DeleteView):
    model = models.Healthcare
    template_name = 'weightapp_cbv/healthcare_confirm_delete.html'
    success_url = reverse_lazy('healthcare_list')
    success_message = '記録が「削除」されました。'

class HealthcareAnalyticsView(View):
    template_name = 'weightapp_cbv/healthcare_analytics.html'
    def get(self,request,*args,**kwargs):
        stats = models.Healthcare.get_eat_three_meals_rate()
        fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,figsize=(12,5)) # グラフの枠組み　一行目2列目

        # ax1 円グラフの作成
        labels = ['eat_three','not_eat_three']
        sizes = [stats['eat_three'],stats['not_eat_three']]
        colors = ['blue','red']
        ax1.pie(sizes,labels = labels,colors = colors,autopct='%1.1f%%',startangle=90)
        ax1.axis('equal')
        ax1.set_title('eat all three meals')

        #折れ線グラフの作成
        df = models.Healthcare.get_healthcares_dataframe()

        if not df.empty:
            x = df['created'].dt.date
            y = df['weight']
            ax2.plot(x,y)
            plt.xticks(rotation=20)
            ax2.set_title('weight change')
            ax2.set_ylabel('weight (kg)')
            ax2.set_xlabel('record date')
            y2 = df['exercise_time']
            ax3.plot(x,y2)
            plt.xticks(rotation=20)
            ax3.set_title('exercise time')
            ax3.set_ylabel('daily exercise time(min)')
            ax3.set_xlabel('record date')
            y3 = df['physical_health']
            y3 = y3.astype(int)
            ax4.plot(x,y3)
            # plt.xticks(rotation=20)
            # ax4.set_yticks([1, 2, 3, 4, 5])
            ax4.set_yticklabels(['poor', 'fair', 'good', 'very good', 'excellent'])

            ax4.set_title('mental health')
            ax4.set_ylabel('5-level rating')
            ax4.set_xlabel('record date')

        # グラフをイメージに変換
        buffer = io.BytesIO()
        plt.tight_layout()
        plt.savefig(buffer,format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        graph = base64.b64encode(image_png).decode('utf-8')

        context = {
            'stats': stats,
            'graph':graph,
        }

        return render(request,self.template_name,context)
