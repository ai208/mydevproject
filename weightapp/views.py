from django.shortcuts import render,redirect,get_object_or_404
from .models import WeightRecord
from .forms import WeightRecordForm

# Create your views here.
# 一覧
def weight_list(request):
    weights = WeightRecord.objects.all()
    return render(request,'weightapp/weight_list.html',{'weight_list':weights})

# 詳細表示
def weight_detail(request,pk):
    target = get_object_or_404(WeightRecord,pk=pk)
    return render(request,'weightapp/weight_detail.html',{'weight':target})

# 新規作成
def weight_create(request):
    if request.method =='POST':
        form = WeightRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('weight_list')
    else:
        form = WeightRecordForm()
    return render(request,'weightapp/weight_form.html',{'form':form,'title':'体重記録'})

# 更新　
def weight_update(request,pk):
    target=get_object_or_404(WeightRecord,pk=pk)
    if request.method=='POST':
        form = WeightRecordForm(request.POST,instance=target)
        if form.is_valid():
            form.save()
            return redirect('weight_list')
    else:
        form=WeightRecordForm(instance=target)
    return render(request,'weightapp/weight_form.html',{'form':form,'title':'記録編集'})

# 削除
def weight_delete(request,pk):
    target=get_object_or_404(WeightRecord,pk=pk)
    if request.method=='POST':
        target.delete()
        return redirect('weight_list')
    return render(request,'weightapp/weight_confirm_delete.html',{'weight':target})
